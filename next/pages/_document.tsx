// https://github.com/newrelic/newrelic-node-nextjs#client-side-instrumentation
const newrelic = require('newrelic');
import Document, {
  DocumentContext,
  DocumentInitialProps,
  Html,
  Head,
  Main,
  NextScript,
} from 'next/document';
import Script from 'next/script';

type DocumentProps = {
  browserTimingHeader: string
}

class MyDocument extends Document<DocumentProps> {
  static async getInitialProps(
    ctx: DocumentContext
  ): Promise<DocumentInitialProps> {
    const initialProps = await Document.getInitialProps(ctx);

    const browserTimingHeader = newrelic.getBrowserTimingHeader({
      hasToRemoveScriptWrapper: true,
    });

    return {
      ...initialProps,
      browserTimingHeader,
    };
  }

  render() {
    const { browserTimingHeader } = this.props

    return (
      <Html>
        <Head>{/* whatever you need here */}</Head>
        <body>
          <Main />
          <NextScript />
          <Script
            dangerouslySetInnerHTML={{ __html: browserTimingHeader }}
            strategy="beforeInteractive"
          ></Script>
        </body>
      </Html>
    );
  }
}

export default MyDocument;
